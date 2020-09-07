from ai_benchmark import AIBenchmark
def main():
  benchmark = AIBenchmark()
  global results
  results = benchmark.run(precision="high")/10
  print(results)
if __name__ == "__main__":
  main()