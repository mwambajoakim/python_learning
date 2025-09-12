"""
Python Enums Coding Test
========================
This test evaluates understanding of Python enums, including basic usage,
functional API, auto values, mixins, and advanced patterns.
Total Points: 100
Time Limit: 45 minutes
"""

from enum import Enum, IntEnum, Flag, IntFlag, auto
from typing import Union
import unittest


# PROBLEM 1: Basic Enum Creation (15 points)
# Create an enum called 'Status' with the following values:
# - PENDING with value 1
# - IN_PROGRESS with value 2  
# - COMPLETED with value 3
# - CANCELLED with value 4

class Status(Enum):
    # TODO: Implement the Status enum
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4


# PROBLEM 2: Enum with Auto Values (10 points)
# Create an enum called 'Priority' using auto() for values:
# - LOW, MEDIUM, HIGH, CRITICAL

class Priority(Enum):
    # TODO: Implement the Priority enum using auto()
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


# PROBLEM 3: String Enum (15 points)
# Create an enum called 'Color' where each member has a string value:
# - RED = "red"
# - GREEN = "green" 
# - BLUE = "blue"
# Add a method called 'hex_code()' that returns the hex color code:
# - RED -> "#FF0000"
# - GREEN -> "#00FF00"
# - BLUE -> "#0000FF"

class Color(Enum):
    # TODO: Implement the Color enum with hex_code method
    pass


# PROBLEM 4: IntEnum Usage (10 points)
# Create an IntEnum called 'HttpStatus' with common HTTP status codes:
# - OK = 200
# - NOT_FOUND = 404
# - INTERNAL_ERROR = 500

class HttpStatus(IntEnum):
    # TODO: Implement the HttpStatus IntEnum
    pass


# PROBLEM 5: Functional API (15 points)
# Use the functional API to create an enum called 'Direction' with members:
# NORTH, SOUTH, EAST, WEST (let Python assign automatic values)

# TODO: Create Direction enum using functional API
Direction = None


# PROBLEM 6: Enum with Methods (20 points)
# Create an enum called 'Planet' with the following data and methods:
# Each planet should store mass (kg) and radius (m)
# 
# Data:
# - MERCURY: mass=3.303e+23, radius=2.4397e6
# - VENUS: mass=4.869e+24, radius=6.0518e6
# - EARTH: mass=5.976e+24, radius=6.37814e6
#
# Methods:
# - surface_gravity(): returns surface gravity in m/s²
#   Formula: G * mass / (radius²) where G = 6.67300E-11
# - __str__(): returns formatted string like "Earth (mass: 5.98e+24 kg, radius: 6.38e+06 m)"

class Planet(Enum):
    # TODO: Implement Planet enum with constructor and methods
    pass


# PROBLEM 7: Flag Enum (15 points)
# Create a Flag enum called 'Permission' for file permissions:
# - READ = 1
# - WRITE = 2  
# - EXECUTE = 4
# Add a class method 'from_octal(octal_str)' that converts octal string to Permission flags
# Example: Permission.from_octal("755") should return READ|WRITE|EXECUTE for owner,
# READ|EXECUTE for group and others

class Permission(Flag):
    # TODO: Implement Permission Flag enum with from_octal method
    pass


# TEST CASES (DO NOT MODIFY)
class TestEnums(unittest.TestCase):
    
    def test_status_enum(self):
        """Test Problem 1: Basic Enum Creation"""
        self.assertEqual(Status.PENDING.value, 1)
        self.assertEqual(Status.IN_PROGRESS.value, 2)
        self.assertEqual(Status.COMPLETED.value, 3)
        self.assertEqual(Status.CANCELLED.value, 4)
        self.assertEqual(len(Status), 4)
    
    def test_priority_enum(self):
        """Test Problem 2: Enum with Auto Values"""
        priorities = list(Priority)
        self.assertEqual(len(priorities), 4)
        self.assertTrue(all(isinstance(p.value, int) for p in priorities))
        self.assertTrue(Priority.LOW.value < Priority.MEDIUM.value)
    
    def test_color_enum(self):
        """Test Problem 3: String Enum"""
        self.assertEqual(Color.RED.value, "red")
        self.assertEqual(Color.GREEN.value, "green")
        self.assertEqual(Color.BLUE.value, "blue")
        self.assertEqual(Color.RED.hex_code(), "#FF0000")
        self.assertEqual(Color.GREEN.hex_code(), "#00FF00")
        self.assertEqual(Color.BLUE.hex_code(), "#0000FF")
    
    def test_http_status_enum(self):
        """Test Problem 4: IntEnum Usage"""
        self.assertEqual(HttpStatus.OK, 200)
        self.assertEqual(HttpStatus.NOT_FOUND, 404)
        self.assertEqual(HttpStatus.INTERNAL_ERROR, 500)
        self.assertTrue(HttpStatus.OK < HttpStatus.NOT_FOUND)
    
    def test_direction_enum(self):
        """Test Problem 5: Functional API"""
        self.assertIsNotNone(Direction)
        self.assertTrue(hasattr(Direction, 'NORTH'))
        self.assertTrue(hasattr(Direction, 'SOUTH'))
        self.assertTrue(hasattr(Direction, 'EAST'))
        self.assertTrue(hasattr(Direction, 'WEST'))
        self.assertEqual(len(Direction), 4)
    
    def test_planet_enum(self):
        """Test Problem 6: Enum with Methods"""
        earth = Planet.EARTH
        self.assertAlmostEqual(earth.surface_gravity(), 9.8, places=0)
        self.assertIn("Earth", str(earth))
        self.assertIn("mass", str(earth))
        self.assertIn("radius", str(earth))
    
    def test_permission_enum(self):
        """Test Problem 7: Flag Enum"""
        self.assertEqual(Permission.READ.value, 1)
        self.assertEqual(Permission.WRITE.value, 2)
        self.assertEqual(Permission.EXECUTE.value, 4)
        
        combined = Permission.READ | Permission.WRITE
        self.assertIn(Permission.READ, combined)
        self.assertIn(Permission.WRITE, combined)
        self.assertNotIn(Permission.EXECUTE, combined)


if __name__ == "__main__":
    print("Python Enums Coding Test")
    print("=" * 50)
    print("Complete the enum implementations above the test cases.")
    print("Run this file to test your solutions.")
    print()
    
    # Run the tests
    unittest.main(verbosity=2)
