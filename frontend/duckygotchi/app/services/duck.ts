import Service from '@ember/service';

export default class DuckService extends Service {
  status: 'exists' | 'dead' | 'unidentified' | undefined;
  duck;

  async main() {
    const duck: null | unknown = await fetch('/api/duck/status').then(
      (data) => {
        if (!data.ok) {
          return null;
        } else {
          return data.json();
        }
      },
    );
    if (!duck) {
      this.status = 'unidentified';
    } else if (Object.keys(duck).length === 0) {
      this.status = 'dead';
    } else {
      this.status = 'exists';
      this.duck = duck;
    }
  }
}

// Don't remove this declaration: this is what enables TypeScript to resolve
// this service using `Owner.lookup('service:duck')`, as well
// as to check when you pass the service name as an argument to the decorator,
// like `@service('duck') declare altName: DuckService;`.
declare module '@ember/service' {
  interface Registry {
    duck: DuckService;
  }
}
