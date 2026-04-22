import React from 'react';

export function BadComponent() {
  let title = "Hello World"; // Fails Biome: should be const
  const unusedData = [1, 2, 3]; // Fails Biome: unused variable

  return (
    <div>
      <h1>{title}</h1>
      {/* Fails Semgrep SAST: Dangerous DOM manipulation */}
      <div dangerouslySetInnerHTML={{ __html: "<script>alert('hack')</script>" }} />
    </div>
  );
}