#!/usr/bin/python3
"""
World Module - Multi-Server Test Utilities
Helper functions for multi-server world module testing
"""

import time

def setup_three_server_network():
    """
    Setup and link 3 servers following _pre_test pattern
    Returns: (m, c1a, c2a, c3a) - test object and clients
    """
    import irctestframework.irctest
    
    # Setup server 1
    m = irctestframework.irctest.IrcTest()
    c1a = m.new('c1a')
    m.connect()
    m.send(c1a, "VERSION")
    m.expect(c1a, "FAKEREPUTATION module loaded", ":.+ 005 .*FAKEREPUTATION")
    m.send(c1a, "OPER netadmin test")
    m.send(c1a, "CONNECT irc2.test.net")
    m.expect(c1a, "irc1<->irc2 linked", "Link irc1.test.net -> irc2.test.net is now synced", timeout=15)
    
    # Setup server 3
    m = irctestframework.irctest.IrcTest()
    c3a = m.new('c3a')
    m.connect()
    m.send(c3a, "VERSION")
    m.expect(c3a, "FAKEREPUTATION module loaded", ":.+ 005 .*FAKEREPUTATION")
    m.send(c3a, "OPER netadmin test")
    m.send(c3a, "CONNECT irc2.test.net")
    m.expect(c3a, "irc3<->irc2 linked", "Link irc3.test.net -> irc2.test.net is now synced", timeout=15)
    
    # Setup server 2
    c2a = m.new('c2a')
    m.connect()
    m.send(c2a, "VERSION")
    m.expect(c2a, "FAKEREPUTATION module loaded", ":.+ 005 .*FAKEREPUTATION")
    
    return m, c1a, c2a, c3a

def verify_sync_across_servers(m, clients, action, expected_pattern, timeout=5):
    """
    Verify that an action on one server is synchronized to all other servers
    Args:
        m: IrcTest object
        clients: dict of {server_name: client} 
        action: function to execute on primary client
        expected_pattern: regex pattern to expect on all servers
        timeout: timeout for expectations
    """
    # Execute action on first client
    action(clients[list(clients.keys())[0]])
    
    # Verify all other clients see the sync
    for server_name, client in clients.items():
        if server_name != list(clients.keys())[0]:  # Skip the one who performed action
            m.expect(client, f"Sync verification on {server_name}", expected_pattern, timeout=timeout)

def test_netsplit_recovery(m, clients, world_channel):
    """
    Test netsplit recovery by parting and rejoining a world channel
    Args:
        m: IrcTest object
        clients: dict of {server_name: client}
        world_channel: channel name to test with
    """
    # Part from world channel
    primary_client = list(clients.values())[0]
    m.send(primary_client, f"WORLD part")
    m.expect(primary_client, "World part success", ":.*2201.*")
    
    # Other clients should see the part
    for server_name, client in clients.items():
        if client != primary_client:
            m.expect(client, f"{server_name} sees part", "WORLD.*PART")
    
    # Rejoin world channel
    m.send(primary_client, f"WORLD join")
    m.expect(primary_client, "World rejoin success", ":.*2200.*")
    
    # Other clients should see the rejoin
    for server_name, client in clients.items():
        if client != primary_client:
            m.expect(client, f"{server_name} sees rejoin", "WORLD.*JOIN")

def verify_message_tags_all_servers(m, clients, tags):
    """
    Verify message tags are present on all servers
    Args:
        m: IrcTest object
        clients: dict of {server_name: client}
        tags: list of tag patterns to verify
    """
    for server_name, client in clients.items():
        for tag_pattern in tags:
            m.expect(client, f"{server_name} sees tag {tag_pattern}", tag_pattern)

def log_server_sync(server, action, details):
    """Log server sync events"""
    print(f"[SYNC] {server}: {action} - {details}")

def log_message_tag(tag_name, tag_value):
    """Log message tag validation"""
    print(f"[TAG] {tag_name}={tag_value}")

def log_multi_client(clients, action):
    """Log multi-client scenarios"""
    client_names = [client.name for client in clients.values()]
    print(f"[MULTI] Clients {client_names}: {action}")

def log_edge_case(scenario, expected, actual):
    """Log edge case results"""
    print(f"[EDGE] {scenario}: expected={expected}, actual={actual}")

def setup_world_capabilities(m, clients):
    """
    Setup world capabilities for all clients
    Args:
        m: IrcTest object
        clients: dict of {server_name: client}
    Returns: True if all clients got ACK, False if any got NAK
    """
    all_acked = True
    
    for server_name, client in clients.items():
        m.send(client, "CAP REQ :world/features")
        resp = m.expect(client, f"{server_name} capability response", ".*ACK.*world/features|.*NAK.*world/features")
        if "NAK" in str(resp):
            print(f"SKIP: World module not loaded on {server_name} - capability NAK'd")
            all_acked = False
        m.clearlog()
    
    return all_acked

def join_world_channel(m, clients, channel_name):
    """
    Join a world channel on all clients
    Args:
        m: IrcTest object
        clients: dict of {server_name: client}
        channel_name: channel to join
    """
    for server_name, client in clients.items():
        m.send(client, f"JOIN {channel_name}")
        m.clearlog()

def verify_world_join_sync(m, clients, joining_client):
    """
    Verify that when one client joins a world, all others see it
    Args:
        m: IrcTest object
        clients: dict of {server_name: client}
        joining_client: client that is joining
    """
    # Send WORLD join command
    m.send(joining_client, "WORLD join")
    m.expect(joining_client, "World join success", ":.*2200.*")
    m.expect(joining_client, "User mode +y set", "MODE.*\\+y")
    
    # All other clients should see the join
    for server_name, client in clients.items():
        if client != joining_client:
            m.expect(client, f"{server_name} sees join", "WORLD.*JOIN")
            m.expect(client, f"{server_name} sees mode +y", "MODE.*\\+y")
    
    m.clearlog()

def verify_movement_sync(m, clients, moving_client, direction):
    """
    Verify that when one client moves, all others see the movement
    Args:
        m: IrcTest object
        clients: dict of {server_name: client}
        moving_client: client that is moving
        direction: direction to move (north, south, east, west)
    """
    # Send MOVE command
    m.send(moving_client, f"MOVE {direction}")
    m.expect(moving_client, "Move success", ":.*2210.*")
    
    # All other clients should see the movement
    for server_name, client in clients.items():
        if client != moving_client:
            m.expect(client, f"{server_name} sees move", "WORLD.*MOVE")
            m.expect(client, f"{server_name} sees location tag", "@world/location=")
            m.expect(client, f"{server_name} sees direction tag", "@world/direction=")
    
    m.clearlog()
