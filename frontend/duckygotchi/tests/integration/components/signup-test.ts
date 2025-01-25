import { module, test } from 'qunit';
import { setupRenderingTest } from 'duckygotchi/tests/helpers';
import { render } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | signup', function (hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`<Signup />`);

    assert.dom().hasText('');

    // Template block usage:
    await render(hbs`
      <Signup>
        template block text
      </Signup>
    `);

    assert.dom().hasText('template block text');
  });
});
