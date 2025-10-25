#!/usr/bin/python3
"""
World Module Test Logging Utilities
Shared logging functions for all world module tests
"""

import time

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
