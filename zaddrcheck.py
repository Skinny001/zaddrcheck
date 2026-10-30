import sys
import json

def validate_address(address: str) -> dict:
    if not address or not isinstance(address, str):
        return {"input": address or "", "valid": False, "type": "invalid"}
    
    address = address.strip()
    
    # Unified Address Check
    if address.startswith("u1") and len(address) >= 100:
        return {"input": address, "valid": True, "type": "unified"}
    
    # Sapling Address Check
    if address.startswith("zs1") and len(address) == 78:
        return {"input": address, "valid": True, "type": "sapling"}
    
    # Transparent Address Check
    if (address.startswith("t1") or address.startswith("t3")) and len(address) == 35:
        return {"input": address, "valid": True, "type": "transparent"}
    
    # Invalid / Malformed / Unknown
    return {"input": address, "valid": False, "type": "invalid"}

def main():
    raw_input = sys.argv[1] if len(sys.argv) > 1 else ""
    result = validate_address(raw_input)
    print(json.dumps(result))

if __name__ == "__main__":
    main()