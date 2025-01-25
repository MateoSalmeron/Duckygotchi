import Component from '@glimmer/component';
import { action } from '@ember/object';

export default class Login extends Component {
  @action submit(event: FormDataEvent) {
    event.preventDefault();
    const formData: FormData = new FormData(event.target);
    console.log(formData);
  }
}
