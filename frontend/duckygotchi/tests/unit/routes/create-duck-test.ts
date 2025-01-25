import { module, test } from 'qunit';
import { setupTest } from 'duckygotchi/tests/helpers';

module('Unit | Route | create-duck', function (hooks) {
  setupTest(hooks);

  test('it exists', function (assert) {
    const route = this.owner.lookup('route:create-duck');
    assert.ok(route);
  });
});
