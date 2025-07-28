require('ts-node').register({
  project: '../tests/frontend/tsconfig.json',
});
module.exports = require('../tests/frontend/jest.config.ts').default;
