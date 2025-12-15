def health():
    return {"status": "ok", "service": "stadium-crowdflow"}

if __name__ == "__main__":
    print(health())
