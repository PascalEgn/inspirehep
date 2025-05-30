export const PUBLISHED_QUERY = { citeable: true, refereed: true };
export const CITEABLE_QUERY = { citeable: true, refereed: undefined };
export const PUBLISHED_BAR_TYPE = 'published';
export const CITEABLE_BAR_TYPE = 'citeable';

export const POST_DOC_RANK_VALUE = 'POSTDOC';
export const CONTACT_URL =
  'https://help.inspirehep.net/knowledge-base/contact-us';
export const RANK_VALUE_TO_DISPLAY = {
  SENIOR: 'Senior (permanent)',
  JUNIOR: 'Junior (leads to Senior)',
  STAFF: 'Staff (non-research)',
  VISITOR: 'Visitor',
  [POST_DOC_RANK_VALUE]: 'PostDoc',
  PHD: 'PhD',
  MASTER: 'Master',
  UNDERGRADUATE: 'Undergrad',
  OTHER: 'Other',
};
export const DEGREE_TYPE_TO_DISPLAY = {
  phd: 'PhD',
  diploma: 'Diploma',
  bachelor: 'Bachelor',
  master: 'Master',
  habilitation: 'Habilitation',
  laurea: 'Laurea',
  other: 'Other',
};

export const AUTHORS_PID_TYPE = 'authors';
export const LITERATURE_PID_TYPE = 'literature';
export const JOBS_PID_TYPE = 'jobs';
export const CONFERENCES_PID_TYPE = 'conferences';
export const INSTITUTIONS_PID_TYPE = 'institutions';
export const SEMINARS_PID_TYPE = 'seminars';
export const EXPERIMENTS_PID_TYPE = 'experiments';
export const JOURNALS_PID_TYPE = 'journals';
export const DATA_PID_TYPE = 'data';

export const INVENIO_URL = '//invenio-software.org';
export const HOLDINGPEN_URL = '/holdingpen';
export const LEGACY_URL = 'https://old.inspirehep.net';
export const AUTHORLIST_TOOL_URL = '/tools/authorlist';
export const INSPIRE_TWITTER_ACCOUNT = 'https://x.com/inspirehep';
export const INSPIRE_BLUESKY_ACCOUNT =
  'https://bsky.app/profile/inspirehep.net';
export const SURVEY_LINK = 'https://forms.gle/ZQi31GvXXHcsgXgM6';
export const FEEDBACK_EMAIL = 'feedback@inspirehep.net';
export const BLOG_URL = 'https://blog.inspirehep.net';
export const HELP_BLOG_URL = 'https://help.inspirehep.net';
export const KNOWLEDGE_BASE_URL = `${HELP_BLOG_URL}/knowledge-base`;
export const ABOUT_INSPIRE_URL = `${KNOWLEDGE_BASE_URL}/about-inspire`;
export const WHAT_IS_ORCID_URL = `${KNOWLEDGE_BASE_URL}/what-is-orcid`;
export const CONTENT_POLICY_URL = `${KNOWLEDGE_BASE_URL}/content-policy`;
export const PRIVACY_NOTICE_URL = `https://cern.service-now.com/service-portal?id=privacy_policy&se=INSPIRE-Online&notice=main`;
export const TERMS_OF_USE_URL = `${KNOWLEDGE_BASE_URL}/terms-of-use`;
export const FAQ_URL = `${KNOWLEDGE_BASE_URL}/faq`;
export const PUBLISHED_URL = `${FAQ_URL}/#faq-published`;
export const PAPER_SEARCH_URL = `${KNOWLEDGE_BASE_URL}/inspire-paper-search`;
export const REPORT_METADATA_URL =
  'https://cern.service-now.com/service-portal?id=sc_cat_item&name=inspire&fe=INSPIRE';

export const DATE_RANGE_FORMAT = 'YYYY-MM-DD';
export const TIME_FORMAT = 'hh:mm A';

export const RANGE_AGGREGATION_SELECTION_SEPARATOR = '--';

export const START_DATE_ALL = 'all';
export const START_DATE_UPCOMING = 'upcoming';
export const START_DATE = 'start_date';
export const DATE_ASC = 'dateasc';
export const DATE_DESC = 'datedesc';
export const CITATION_COUNT_PARAM = 'citation_count';
export const CITATION_COUNT_WITHOUT_SELF_CITATIONS_PARAM =
  'citation_count_without_self_citations';

export const SEARCH_PAGE_GUTTER = { xs: 0, lg: 32 };
export const SEARCH_PAGE_COL_SIZE_WITH_FACETS = {
  xs: 24,
  lg: 22,
  xl: 20,
  xxl: 18,
};
export const SEARCH_PAGE_COL_SIZE_WITHOUT_FACETS = {
  xs: 24,
  lg: 16,
  xl: 16,
  xxl: 14,
};
export const SEARCH_PAGE_COL_SIZE_NO_RESULTS = { xs: 24 };

export const LOCAL_TIMEZONE =
  Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
