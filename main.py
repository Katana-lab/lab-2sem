from src.wire_length9 import max_wire_length

if __name__ == "__main__":
    w = int(input())
    heights = list(map(int, input().split()))
    print(f"{max_wire_length(w, heights):.2f}")
