import { module, test } from 'qunit';
import { setupRenderingTest } from 'duckygotchi/tests/helpers';
import { render } from '@ember/test-helpers';
import { hbs } from 'ember-cli-htmlbars';

module('Integration | Component | create-duck', function (hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`<CreateDuck />`);

    assert.dom().hasText('');

    // Template block usage:
    await render(hbs`
      <CreateDuck>
        template block text
      </CreateDuck>
    `);

    assert.dom().hasText('template block text');
  });
});
