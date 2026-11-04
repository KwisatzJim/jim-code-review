export function apply(current, submitted, saved) {
  return current.id === submitted.id && current.content === submitted.content
    ? { ...current, modified_at: saved.modified_at }
    : current;
}
