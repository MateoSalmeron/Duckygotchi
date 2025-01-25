import Component from '@glimmer/component';
import { action } from '@ember/object';
import { service } from '@ember/service';

export default class CreateDuck extends Component {
  @service router;
  error;
  
  @action async submit(event: FormDataEvent) {
    event.preventDefault();
    this.error = '';
    const formData: FormData = new FormData(event.target);
    const duckName = formData.get('duckName');
    if(!duckName){
      return;
    }
    const finish = await fetch('/api/duck/create/' + duckName).then(data => data.ok);
    if(finish){
      this.router.transitionTo('/');
    }else{
      this.error = 'Unspecified error';
    }
  }
}
