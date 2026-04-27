import { render, screen } from "@testing-library/react";
import { expect, test } from "vitest";
import { App } from "./App";
import React from "react";

test("renders App correctly", () => {
	render(<App title="Hello React" />);
	expect(screen.getByText("Hello React")).toBeDefined();
});

test("renders Error state", () => {
	render(<App title="Error" />);
	expect(screen.getByText("Error State")).toBeDefined();
});
