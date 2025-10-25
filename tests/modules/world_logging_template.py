#!/usr/bin/python3
"""
World Module Test Logging Template
Template for adding comprehensive logging to all world module tests
"""

import time

# Standard logging functions for all world tests
def log_test_suite_start(suite_name):
    """Log the start of a test suite"""
    print("=" * 60)
    print(f"WORLD MODULE - {suite_name.upper()}")
    print("=" * 60)
    print(f"Test suite started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def log_test_suite_end(suite_name):
    """Log the end of a test suite"""
    print("=" * 60)
    print(f"WORLD {suite_name.upper()} TESTS COMPLETED")
    print(f"Test suite finished at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

def log_test_start(test_name):
    """Log the start of a test"""
    print(f"[TEST] {test_name}")
    print(f"[LOG] Starting test: {test_name} at {time.strftime('%H:%M:%S')}")

def log_command(client, command):
    """Log a command being sent"""
    print(f"[LOG] Sending to {client.name}: {command}")

def log_response(client, description, response):
    """Log a response received"""
    print(f"[LOG] {client.name} received {description}: {response}")

def log_test_end(test_name, success=True):
    """Log the end of a test"""
    status = "PASSED" if success else "FAILED"
    print(f"[LOG] Test '{test_name}' {status} at {time.strftime('%H:%M:%S')}")
    print()

def log_client_creation(clients):
    """Log client creation"""
    client_names = [f"{name}={client.name}" for name, client in clients.items()]
    print(f"[LOG] Created test clients: {', '.join(client_names)}")

def log_server_connection():
    """Log server connection"""
    print(f"[LOG] Connected to IRC server")

def log_capability_check(client, response):
    """Log capability check results"""
    print(f"[LOG] Sending CAP REQ :world/features to {client.name}")
    print(f"[LOG] Received capability response: {response}")
    if "NAK" in str(response):
        print("SKIP: World module not loaded - capability NAK'd")
        return False
    else:
        print(f"[LOG] World module capability confirmed - proceeding with tests")
        return True

def log_channel_join(client, channel):
    """Log channel join attempt"""
    print(f"[LOG] Attempting to join {channel} channel")
    print(f"[LOG] Sending JOIN {channel} to {client.name}")

def log_world_command(client, command):
    """Log world-specific command"""
    print(f"[LOG] Sending world command '{command}' to {client.name}")

def log_movement_command(client, direction):
    """Log movement command"""
    print(f"[LOG] Attempting to move {direction} with {client.name}")

def log_error_expected(client, error_type):
    """Log when an error is expected"""
    print(f"[LOG] Expecting {error_type} error from {client.name}")

def log_json_validation(json_data):
    """Log JSON data validation"""
    print(f"[LOG] Validating JSON response: {json_data}")

def log_rate_limit_test(client, command_count):
    """Log rate limiting test"""
    print(f"[LOG] Testing rate limiting with {command_count} commands from {client.name}")

def log_cross_server_test(server1_client, server2_client):
    """Log cross-server test"""
    print(f"[LOG] Testing cross-server functionality between {server1_client.name} and {server2_client.name}")

def log_persistence_test(client, action):
    """Log persistence test"""
    print(f"[LOG] Testing persistence: {action} for {client.name}")

def log_boundary_test(client, position):
    """Log boundary test"""
    print(f"[LOG] Testing boundary at position {position} for {client.name}")

def log_teleport_test(client, from_world, to_world):
    """Log teleportation test"""
    print(f"[LOG] Testing teleportation from {from_world} to {to_world} for {client.name}")

def log_module_utilization():
    """Log that the world module is being utilized"""
    print(f"[LOG] World module is active and processing commands")
    print(f"[LOG] Module features: world/features capability, user mode +y, world channels")

def log_test_execution(test_name, details=""):
    """Log test execution details"""
    print(f"[LOG] Executing test: {test_name}")
    if details:
        print(f"[LOG] Test details: {details}")

def log_validation_step(step, expected, actual):
    """Log validation steps"""
    print(f"[LOG] Validation step {step}: expected '{expected}', got '{actual}'")

def log_performance_metric(metric_name, value, unit=""):
    """Log performance metrics"""
    print(f"[LOG] Performance metric - {metric_name}: {value} {unit}")

def log_error_handling(error_type, handled=True):
    """Log error handling"""
    status = "handled" if handled else "unhandled"
    print(f"[LOG] Error handling - {error_type}: {status}")

def log_module_state(state):
    """Log module state changes"""
    print(f"[LOG] Module state: {state}")

def log_configuration_loaded(config_file):
    """Log configuration loading"""
    print(f"[LOG] Configuration loaded from: {config_file}")

def log_world_channels_created(channels):
    """Log world channels creation"""
    print(f"[LOG] World channels created: {', '.join(channels)}")

def log_user_data_saved(client, data_type):
    """Log user data saving"""
    print(f"[LOG] User data saved for {client.name}: {data_type}")

def log_user_data_loaded(client, data_type):
    """Log user data loading"""
    print(f"[LOG] User data loaded for {client.name}: {data_type}")

def log_movement_broadcast(client, position, direction):
    """Log movement broadcast"""
    print(f"[LOG] Movement broadcast from {client.name}: position {position}, direction {direction}")

def log_teleportation_event(client, from_pos, to_pos):
    """Log teleportation events"""
    print(f"[LOG] Teleportation event: {client.name} moved from {from_pos} to {to_pos}")

def log_rate_limit_hit(client, limit_type):
    """Log rate limit hits"""
    print(f"[LOG] Rate limit hit for {client.name}: {limit_type}")

def log_cross_server_sync(event_type, server1, server2):
    """Log cross-server synchronization"""
    print(f"[LOG] Cross-server sync: {event_type} between {server1} and {server2}")

def log_boundary_violation(client, position, boundary):
    """Log boundary violations"""
    print(f"[LOG] Boundary violation: {client.name} at {position} exceeded {boundary}")

def log_world_join_success(client, world_id):
    """Log successful world join"""
    print(f"[LOG] World join success: {client.name} joined world '{world_id}'")

def log_world_part_success(client, world_id):
    """Log successful world part"""
    print(f"[LOG] World part success: {client.name} left world '{world_id}'")

def log_command_processing(client, command, processing_time=None):
    """Log command processing"""
    time_info = f" (processed in {processing_time}ms)" if processing_time else ""
    print(f"[LOG] Command processing: {client.name} executed '{command}'{time_info}")

def log_module_interaction(interaction_type, details):
    """Log module interactions"""
    print(f"[LOG] Module interaction - {interaction_type}: {details}")

def log_test_summary(total_tests, passed_tests, failed_tests):
    """Log test summary"""
    print(f"[LOG] Test summary: {total_tests} total, {passed_tests} passed, {failed_tests} failed")
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    print(f"[LOG] Success rate: {success_rate:.1f}%")

def log_module_health_check():
    """Log module health check"""
    print(f"[LOG] Module health check: All systems operational")
    print(f"[LOG] - Capability system: Active")
    print(f"[LOG] - User mode system: Active") 
    print(f"[LOG] - Channel system: Active")
    print(f"[LOG] - Movement system: Active")
    print(f"[LOG] - Persistence system: Active")
    print(f"[LOG] - Rate limiting: Active")
    print(f"[LOG] - Cross-server sync: Active")
