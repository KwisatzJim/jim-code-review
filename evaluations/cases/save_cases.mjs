// A returned server snapshot is older than the editor if typing continued.
export function acknowledge(current, submitted, saved) {
  return saved;
}

export function acknowledgeSafe(current, submitted, saved) {
  return current.id === submitted.id && current.content === submitted.content
    ? { ...current, modified_at: saved.modified_at }
    : current;
}
