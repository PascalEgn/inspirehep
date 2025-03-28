import { render } from '@testing-library/react';
import { MemoryRouter, Route, Switch } from 'react-router-dom';

import RouteOrRedirect from '../RouteOrRedirect';

const Test = () => <div>Test Component</div>;

describe('RouteOrRedirect', () => {
  it('renders component if condition is true', () => {
    const { getByText } = render(
      <MemoryRouter initialEntries={['/test']} initialIndex={0}>
        <Switch>
          <RouteOrRedirect
            exact
            path="/test"
            condition
            component={Test}
            redirectTo="/nowhere"
          />
        </Switch>
      </MemoryRouter>
    );
    expect(getByText('Test Component')).toBeInTheDocument();
  });

  it('redirects if condition is false', () => {
    const Another = () => <div>Another Component</div>;
    const { queryByText, getByText } = render(
      <MemoryRouter initialEntries={['/test']} initialIndex={0}>
        <Switch>
          <Route exact path="/another" component={Another} />
          <RouteOrRedirect
            exact
            path="/test"
            condition={false}
            component={Test}
            redirectTo="/another"
          />
        </Switch>
      </MemoryRouter>
    );

    expect(getByText('Another Component')).toBeInTheDocument();
    expect(queryByText('Test Component')).toBeNull();
  });
});
