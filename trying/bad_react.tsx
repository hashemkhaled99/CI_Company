import { render, screen } from "@testing-library/react";
import { expect, test } from "vitest";
import App from "./App";

test("renders the Sijil-CI welcome message", () => {
  render(<App />);
  // Adjust "Welcome" to match whatever text is actually in your App.tsx
  const linkElement = screen.getByText(/Welcome/i);
  expect(linkElement).toBeDefined();
});