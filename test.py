#!/usr/bin/env python3
# test.py – Mock tests for the Ops Analyzer logic

# -------------------------------------------------------------------
# 1. KPI Function (copied from notebook)
# -------------------------------------------------------------------
def calculate_efficiency(actual_output, target_output):
    """Return efficiency percentage; avoid division by zero."""
    if target_output == 0:
        return 0.0
    return (actual_output / target_output) * 100

# -------------------------------------------------------------------
# 2. Status Classifier (copied from notebook)
# -------------------------------------------------------------------
def get_operational_status(efficiency):
    """Classify efficiency into Critical / Warning / Normal."""
    if efficiency < 70:
        return "Critical"
    elif efficiency < 90:
        return "Warning"
    else:
        return "Normal"

# -------------------------------------------------------------------
# 3. Mock data – same as in the notebook
# -------------------------------------------------------------------
MOCK_SITES = [
    {"name": "North Depot", "actual_output": 8200, "target_output": 10000},
    {"name": "South Depot", "actual_output": 6500, "target_output": 8000},
    {"name": "East Depot",  "actual_output": 9500, "target_output": 10000},
]

# -------------------------------------------------------------------
# 4. Test runner
# -------------------------------------------------------------------
def run_tests():
    print("=" * 60)
    print("RUNNING MOCK TESTS FOR OPS ANALYZER")
    print("=" * 60)

    # ---- Test 1: calculate_efficiency ----
    print("\n[Test 1] calculate_efficiency")
    cases = [
        (100, 200, 50.0),
        (80, 100, 80.0),
        (0, 100, 0.0),
        (50, 0, 0.0),   # target zero -> returns 0.0
    ]
    for actual, target, expected in cases:
        result = calculate_efficiency(actual, target)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"  {actual}/{target} -> {result} (expected {expected}) {status}")

    # ---- Test 2: get_operational_status ----
    print("\n[Test 2] get_operational_status")
    cases = [
        (65, "Critical"),
        (70, "Warning"),    # threshold: 70 is Warning
        (89, "Warning"),
        (90, "Normal"),
        (95, "Normal"),
    ]
    for eff, expected in cases:
        result = get_operational_status(eff)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"  {eff}% -> '{result}' (expected '{expected}') {status}")

    # ---- Test 3: Full mock report ----
    print("\n[Test 3] Full mock report (same as notebook output)")
    print("-" * 60)
    for site in MOCK_SITES:
        name = site["name"]
        actual = site["actual_output"]
        target = site["target_output"]
        eff = calculate_efficiency(actual, target)
        status = get_operational_status(eff)
        print(f"{name:12} | Actual: {actual:5} | Target: {target:5} | "
              f"Efficiency: {eff:5.1f}% | Status: {status}")
    print("-" * 60)
    print("Mock tests completed.\n")

if __name__ == "__main__":
    run_tests()