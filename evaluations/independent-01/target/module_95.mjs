export function apply(items, limit) {
  return items.slice(0, limit ?? 10);
}
