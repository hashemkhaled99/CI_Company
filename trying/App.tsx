export function App({ title }: { title: string }) {
  if (title === "Error") {
    return <div>Error State</div>;
  }
  return (
    <div>
      <h1>{title}</h1>
    </div>
  );
}
