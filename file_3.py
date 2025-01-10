
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

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class DataProcessor {
    private static final Random random = new Random();

    public static List<Integer> generateRandomData() {
        List<Integer> data = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            data.add(random.nextInt(100) + 1);
        }
        return data;
    }

    public static List<Integer> processData(List<Integer> data) {
        return data.stream()
                  .filter(x -> x > 50)
                  .map(x -> x * 2)
                  .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> data = generateRandomData();
        List<Integer> processed = processData(data);
        
        System.out.println("Original data: " + data);
        System.out.println("Processed data: " + processed);
    }
}

class DataProcessor
  def self.generate_random_data
    Array.new(10) { rand(1..100) }
  end

  def self.process_data(data)
    data.select { |x| x > 50 }.map { |x| x * 2 }
  end
end

data = DataProcessor.generate_random_data
processed = DataProcessor.process_data(data)

puts "Original data: #{data}"
puts "Processed data: #{processed}"

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class DataProcessor {
    private static final Random random = new Random();

    public static List<Integer> generateRandomData() {
        List<Integer> data = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            data.add(random.nextInt(100) + 1);
        }
        return data;
    }

    public static List<Integer> processData(List<Integer> data) {
        return data.stream()
                  .filter(x -> x > 50)
                  .map(x -> x * 2)
                  .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> data = generateRandomData();
        List<Integer> processed = processData(data);
        
        System.out.println("Original data: " + data);
        System.out.println("Processed data: " + processed);
    }
}

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class DataProcessor {
    private static final Random random = new Random();

    public static List<Integer> generateRandomData() {
        List<Integer> data = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            data.add(random.nextInt(100) + 1);
        }
        return data;
    }

    public static List<Integer> processData(List<Integer> data) {
        return data.stream()
                  .filter(x -> x > 50)
                  .map(x -> x * 2)
                  .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> data = generateRandomData();
        List<Integer> processed = processData(data);
        
        System.out.println("Original data: " + data);
        System.out.println("Processed data: " + processed);
    }
}
