import { bench, describe } from "vitest";

describe("React Benchmark", () => {
  bench("simple logic operation", () => {
    let _result = 0;
    for (let i = 0; i < 1000; i++) {
      _result += i;
    }
  });
});
