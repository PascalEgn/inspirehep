import React, { MouseEventHandler } from 'react';
import { Link } from 'react-router-dom';
import { Menu, Tooltip, Button } from 'antd';

import {
  SUBMISSIONS_AUTHOR,
  USER_LOGIN,
  SUBMISSIONS_JOB,
  SUBMISSIONS_LITERATURE,
  SUBMISSIONS_CONFERENCE,
  SUBMISSIONS_SEMINAR,
  SUBMISSIONS_INSTITUTION,
  SUBMISSIONS_EXPERIMENT,
  SUBMISSIONS_JOURNAL,
  USER_SETTINGS,
} from '../../routes';
import LinkWithTargetBlank from '../../components/LinkWithTargetBlank';
import LinkLikeButton from '../../components/LinkLikeButton/LinkLikeButton';

import './HeaderMenu.less';
import { PAPER_SEARCH_URL, HELP_BLOG_URL } from '../../constants';
import DisplayGuideButtonContainer from '../../containers/DisplayGuideButtonContainer';
import { CLAIMING_DISABLED_INFO } from '../../../authors/components/AssignNoProfileAction';

const HeaderMenu = ({
  loggedIn,
  onLogoutClick,
  isCatalogerLoggedIn,
  profileControlNumber,
}: {
  loggedIn: boolean;
  onLogoutClick: MouseEventHandler<HTMLElement>;
  isCatalogerLoggedIn: boolean;
  profileControlNumber: string;
}) => {
  const USER_PROFILE_URL = `/authors/${profileControlNumber}`;

  return (
    <Menu
      className="__HeaderMenu__"
      theme="dark"
      mode="horizontal"
      selectable={false}
    >
      <Menu.SubMenu
        key="help"
        title="Help"
        popupClassName="header-submenu ant-menu-dark"
      >
        <Menu.Item key="help.search-tips">
          <LinkWithTargetBlank href={PAPER_SEARCH_URL}>
            Search Tips
          </LinkWithTargetBlank>
        </Menu.Item>
        <Menu.Item key="help.tour">
          <DisplayGuideButtonContainer color="white">
            Take the tour
          </DisplayGuideButtonContainer>
        </Menu.Item>
        <Menu.Item key="help.help-center">
          <LinkWithTargetBlank href={HELP_BLOG_URL}>
            Help Center
          </LinkWithTargetBlank>
        </Menu.Item>
      </Menu.SubMenu>

      <Menu.SubMenu
        key="submit"
        title="Submit"
        popupClassName="header-submenu ant-menu-dark"
      >
        <Menu.Item key="submit.literature">
          <Link to={SUBMISSIONS_LITERATURE}>Literature</Link>
        </Menu.Item>
        <Menu.Item key="submit.author">
          <Link to={SUBMISSIONS_AUTHOR}>Author</Link>
        </Menu.Item>
        <Menu.Item key="submit.job">
          <Link to={SUBMISSIONS_JOB}>Job</Link>
        </Menu.Item>
        <Menu.Item key="submit.seminar">
          <Link to={SUBMISSIONS_SEMINAR}>Seminar</Link>
        </Menu.Item>
        <Menu.Item key="submit.conference">
          <Link to={SUBMISSIONS_CONFERENCE}>Conference</Link>
        </Menu.Item>
        {isCatalogerLoggedIn && (
          <Menu.Item key="submit.institution">
            <Link to={SUBMISSIONS_INSTITUTION}>Institution</Link>
          </Menu.Item>
        )}
        {isCatalogerLoggedIn && (
          <Menu.Item key="submit.experiment">
            <Link to={SUBMISSIONS_EXPERIMENT}>Experiment</Link>
          </Menu.Item>
        )}
        {isCatalogerLoggedIn && (
          <Menu.Item key="submit.journal">
            <Link to={SUBMISSIONS_JOURNAL}>Journal</Link>
          </Menu.Item>
        )}
      </Menu.SubMenu>
      {loggedIn ? (
        <Menu.SubMenu
          key="account"
          title="Account"
          popupClassName="header-submenu ant-menu-dark"
          data-test-id="account"
        >
          <Menu.Item key="my-profile">
            {profileControlNumber ? (
              <Link to={USER_PROFILE_URL}>My profile</Link>
            ) : (
              <Tooltip title={CLAIMING_DISABLED_INFO}>
                <Button ghost disabled>
                  My profile
                </Button>
              </Tooltip>
            )}
          </Menu.Item>
          <Menu.Item key="settings">
            <Link to={USER_SETTINGS}>Settings</Link>
          </Menu.Item>
          <Menu.Item key="logout">
            <LinkLikeButton
              onClick={onLogoutClick}
              dataTestId="logout"
              color="white"
            >
              Logout
            </LinkLikeButton>
          </Menu.Item>
        </Menu.SubMenu>
      ) : (
        <Menu.Item key="login">
          <Link to={USER_LOGIN}>Login</Link>
        </Menu.Item>
      )}
    </Menu>
  );
};

export default HeaderMenu;