import React from 'react';
import { shallow } from 'enzyme';
import { fromJS } from 'immutable';

import ConferenceSeries from '../ConferenceSeries';

describe('ConferenceSeries', () => {
  it('renders with only name', () => {
    const series = fromJS({ name: 'Conference Name' });
    const wrapper = shallow(<ConferenceSeries series={series} />);
    expect(wrapper).toMatchSnapshot();
  });
  it('renders with name and number', () => {
    const series = fromJS({ name: 'Conference Name', number: 10 });
    const wrapper = shallow(<ConferenceSeries series={series} />);
    expect(wrapper).toMatchSnapshot();
  });
});