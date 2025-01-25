import { module, test } from 'qunit';
import { setupTest } from 'duckygotchi/tests/helpers';

module('Unit | Route | signup', function (hooks) {
  setupTest(hooks);

  test('it exists', function (assert) {
    const route = this.owner.lookup('route:signup');
    assert.ok(route);
  });
});
