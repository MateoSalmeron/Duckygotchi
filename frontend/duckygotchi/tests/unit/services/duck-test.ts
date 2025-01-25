import { module, test } from 'qunit';
import { setupTest } from 'duckygotchi/tests/helpers';

module('Unit | Service | duck', function (hooks) {
  setupTest(hooks);

  // TODO: Replace this with your real tests.
  test('it exists', function (assert) {
    const service = this.owner.lookup('service:duck');
    assert.ok(service);
  });
});
