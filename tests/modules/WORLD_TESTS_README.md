# World Module Test Suite

Comprehensive test suite for the UnrealIRCd World Module (`third/world`).

## Test Files

8 test suites covering all aspects of the world module:

### Core Functionality
- **world_basic** (12 tests) - Capability negotiation, join/part, movement, JSON validation, message tags
- **world_commands** (18 tests) - All command variations, error conditions, case-insensitivity

### Advanced Features
- **world_boundaries** (14 tests) - Movement limits, boundary validation, position tracking
- **world_teleport** (12 tests) - Exit/entrance points, cross-world teleportation, channel transitions
- **world_modes** (16 tests) - Channel mode +W, user mode +w, access control
- **world_persistence** (10 tests) - Save/load functionality, position restoration, JSON storage
- **world_ratelimit** (13 tests) - Move and command rate limiting, per-user limits
- **world_cross_server** (18 tests) - Multi-server synchronization, message tag propagation

**Total: 113+ test scenarios**

## Running Tests

Run all world tests:
```bash
cd unrealircd-tests
./run -services none -boot tests/modules/world_*
```

Run specific test suite:
```bash
./run -services none -boot tests/modules/world_basic
./run -services none -boot tests/modules/world_commands
./run -services none -boot tests/modules/world_boundaries
./run -services none -boot tests/modules/world_teleport
./run -services none -boot tests/modules/world_modes
./run -services none -boot tests/modules/world_persistence
./run -services none -boot tests/modules/world_ratelimit
./run -services none -boot tests/modules/world_cross_server
```

Run with debugging:
```bash
./run -services none -boot -debug tests/modules/world_basic
```

## Prerequisites

1. **Compile world module:**
   ```bash
   cd src/modules/third/world
   make clean && make all
   cd ../../..
   make install
   ```

2. **Load module in config:**
   ```conf
   loadmodule "third/world";
   ```

3. **Configure module** (`unrealircd.conf`):
   ```conf
   world {
       config-file "conf/worlds.json";
       user-data-dir "data/world/users";
       autosave-interval 1800;
       move-rate-limit 2;
       command-rate-limit 5;
   };
   ```

4. **Create world configuration** (`conf/worlds.json`):
   ```json
   {
     "worlds": {
       "spawn": {
         "width": 10,
         "height": 10,
         "respawn": {
           "x": 5,
           "y": 5,
           "direction": "north"
         },
         "exits": [
           {
             "x": 9,
             "y": 5,
             "target_world": "forest",
             "target_entrance": "spawn_exit"
           }
         ],
         "entrances": [
           {
             "id": "from_forest",
             "x": 1,
             "y": 5,
             "direction": "west"
           }
         ]
       },
       "forest": {
         "width": 15,
         "height": 15,
         "respawn": {
           "x": 7,
           "y": 7,
           "direction": "south"
         },
         "exits": [
           {
             "x": 1,
             "y": 7,
             "target_world": "spawn",
             "target_entrance": "from_forest"
           }
         ],
         "entrances": [
           {
             "id": "spawn_exit",
             "x": 14,
             "y": 7,
             "direction": "east"
           }
         ]
       }
     }
   }
   ```

## World Commands Reference

### Game Management
| Command | Description | Example |
|---------|-------------|---------|
| `WORLD join` | Join the world in current channel | `WORLD join` |
| `WORLD part` | Leave the world | `WORLD part` |
| `WORLD show` | Show current world information | `WORLD show` |

### Movement
| Command | Description | Example |
|---------|-------------|---------|
| `MOVE <dir>` | Move in direction | `MOVE north` |
| `FACE <dir>` | Change facing direction | `FACE east` |

### Directions
- `north` - Move/face north
- `south` - Move/face south
- `east` - Move/face east
- `west` - Move/face west

## Protocol Numerics

### Success Responses (2200-2229)
- **2200** (RPL_WORLDJOIN) - Join success with JSON (world_id, x, y, direction)
- **2201** (RPL_WORLDPART) - Part success with JSON (channel, world_id)
- **2202** (RPL_WORLDINFO) - World info with JSON (world_id, width, height, x, y, direction)
- **2210** (RPL_WORLDMOVE) - Move success with JSON (x, y, direction)
- **2211** (RPL_WORLDFACE) - Face success with JSON (direction, x, y)

### Error Responses (2240-2259)
- **2240** (ERR_WORLDNOCAP) - Missing world/features capability
- **2241** (ERR_WORLDRATELIMIT) - Rate limit exceeded
- **2242** (ERR_WORLDBOUNDS) - Out of bounds or invalid direction
- **2243** (ERR_WORLDNOWORLD) - No world configured or not in channel
- **2244** (ERR_WORLDNOTINWORLD) - Not in world
- **2245** (ERR_WORLDALREADYIN) - Already in world
- **2246** (ERR_WORLDNEEDMODE) - Need mode/capability

## IRCv3 Features

### Capabilities
- **world/features** - Required to join world channels

### Channel Modes
- **+W** - World channel mode (requires world_id parameter)

### User Modes
- **+w** - World user mode (auto-set on WORLD join, auto-removed on WORLD part)

### Message Tags
- **world/location** - User's current position (x,y)
- **world/direction** - User's facing direction (north/south/east/west)
- **world/grid** - Grid information (reserved for future use)

## Test Coverage Summary

### Basic Functionality ✓
- [x] Capability negotiation
- [x] WORLD join/part/show commands
- [x] MOVE command (all 4 directions)
- [x] FACE command (all 4 directions)
- [x] JSON response validation
- [x] Message tag verification
- [x] Multiple users in world

### Commands ✓
- [x] All command variations
- [x] Error conditions
- [x] Case-insensitivity
- [x] Parameter validation
- [x] Usage messages

### Boundaries ✓
- [x] Valid movement within bounds
- [x] Boundary edge detection
- [x] Out-of-bounds prevention
- [x] Spawn point validation
- [x] Position tracking
- [x] Direction changes

### Teleportation ✓
- [x] Exit point triggers teleport
- [x] Entrance sets correct position
- [x] Cross-world movement
- [x] Channel auto-JOIN/PART
- [x] Multiple exits/entrances
- [x] Position preservation

### Modes ✓
- [x] Channel mode +W with parameter
- [x] Operator-only mode setting
- [x] User mode +w auto-set/remove
- [x] Mode broadcasting
- [x] Access control enforcement
- [x] Multiple world channels

### Persistence ✓
- [x] Position saved on WORLD part
- [x] Position loaded on WORLD join
- [x] Direction preservation
- [x] Reconnect handling
- [x] Multiple users independent saves
- [x] JSON format validation

### Rate Limiting ✓
- [x] MOVE rate limit (2/second default)
- [x] Command rate limit (5/second default)
- [x] Rate limit exceeded errors
- [x] Per-user rate limits
- [x] Separate move/command limits
- [x] Limit reset mechanisms

### Cross-Server ✓
- [x] Join broadcast synchronization
- [x] Move synchronization
- [x] Face synchronization
- [x] Mode synchronization
- [x] Message tag propagation
- [x] Multi-user visibility
- [x] Server split handling

## Debugging Failed Tests

**Check server logs:**
```bash
tail -f ~/unrealircd/logs/ircd.log
```

**Verify module is loaded:**
```bash
./unrealircd module list | grep world
```

**Test manually with IRC client:**
```
/CAP REQ :world/features
/JOIN #spawn
/MODE #spawn +W spawn
/WORLD join
/MOVE north
/FACE east
/WORLD show
/WORLD part
```

## Common Issues

**Module not loaded:**
- Check that `loadmodule "third/world";` is in config
- Verify `world.so` exists in `modules/third/`
- Check for module load errors in ircd.log

**Tests fail with "Not in world" errors:**
- Ensure capability is requested (`CAP REQ :world/features`)
- Check that channel has +W mode set
- Verify worlds.json is configured correctly

**Rate limit tests fail:**
- Adjust rate limits in config if needed
- Tests assume default values (2 moves/sec, 5 commands/sec)

**Cross-server tests fail:**
- Ensure servers are linked in test config
- Check server-to-server protocol messages
- Verify broadcast messages propagate

## Configuration Examples

### worlds.json
Complete example with spawn and forest worlds:
```json
{
  "worlds": {
    "spawn": {
      "width": 10,
      "height": 10,
      "respawn": { "x": 5, "y": 5, "direction": "north" },
      "exits": [
        { "x": 9, "y": 5, "target_world": "forest", "target_entrance": "spawn_exit" }
      ],
      "entrances": [
        { "id": "from_forest", "x": 1, "y": 5, "direction": "west" }
      ]
    },
    "forest": {
      "width": 15,
      "height": 15,
      "respawn": { "x": 7, "y": 7, "direction": "south" },
      "exits": [
        { "x": 1, "y": 7, "target_world": "spawn", "target_entrance": "from_forest" }
      ],
      "entrances": [
        { "id": "spawn_exit", "x": 14, "y": 7, "direction": "east" }
      ]
    }
  }
}
```

---

*Last updated: 2025-10-25 - World Module Test Suite v1.0*

