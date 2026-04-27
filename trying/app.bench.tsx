import { bench, describe } from "vitest";

describe("React Benchmark", () => {
  bench("simple logic operation", () => {
    let result = 0;
    for (let i = 0; i < 1000; i++) {
      result += i;
    }
  });
});
