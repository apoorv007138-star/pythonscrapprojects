"""Demonstrate useful dictionary operations."""
student = {"name": "Avery", "course": "Python", "score": 88}

print("Original:", student)
print("Name:", student.get("name"))
student.update({"score": 92, "active": True})
print("Updated:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:")
for key, value in student.items():
    print(f"  {key}: {value}")

removed = student.pop("active", False)
print("Removed active flag:", removed)
print("Final:", student)
