
import random
from typing import List

def generate_random_data() -> List[int]:
    data = [random.randint(1, 100) for _ in range(10)]
    return data

def process_data(data: List[int]) -> List[int]:
    return [x * 2 for x in data if x > 50]

def main() -> None:
    data = generate_random_data()
    processed = process_data(data)
    print(f"Original data: {data}")
    print(f"Processed data: {processed}")

if __name__ == "__main__":
    main()

function generateRandomData() {
    return Array.from({ length: 10 }, () => 
        Math.floor(Math.random() * 100) + 1
    );
}

function processData(data) {
    return data
        .filter(x => x > 50)
        .map(x => x * 2);
}

function main() {
    const data = generateRandomData();
    const processed = processData(data);
    
    console.log("Original data:", data);
    console.log("Processed data:", processed);
}

main();
