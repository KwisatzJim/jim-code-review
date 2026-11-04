import test from 'node:test';
import assert from 'node:assert/strict';
import { acknowledge, acknowledgeSafe } from './cases/save_cases.mjs';
const submitted = { id: 1, content: 'old', modified_at: 1 };
const current = { id: 1, content: 'new', modified_at: 1 };
const saved = { ...submitted, modified_at: 2 };
test('unsafe acknowledgment loses the newer edit', () => {
  assert.equal(acknowledge(current, submitted, saved).content, 'old');
});
test('guarded acknowledgment preserves the newer edit', () => {
  assert.equal(acknowledgeSafe(current, submitted, saved).content, 'new');
  assert.equal(acknowledgeSafe(submitted, submitted, saved).modified_at, 2);
});
