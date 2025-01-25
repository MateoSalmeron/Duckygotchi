import { service } from '@ember/service';
import Component from '@glimmer/component';
import DuckService from 'duckygotchi/services/duck';

export default class Index extends Component {
  @service('duck') duckService: DuckService;
  @service router;

  constructor() {
    super(...arguments);
    this.main();
  }

  async main() {
    await this.duckService.main();
    if (this.duckService.status === 'unidentified') {
      this.router.transitionTo('login');
    } else if (this.duckService.status === 'dead') {
      this.router.transitionTo('create-duck');
    }
  }
}
