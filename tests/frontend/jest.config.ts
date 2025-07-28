const path = require('path');
const { defaultsESM } = require(path.join(__dirname, '../../frontend/node_modules/ts-jest/presets/default-esm/jest-preset')); 

module.exports = {
  ...defaultsESM,
  roots: ['<rootDir>/react-testing-library'],
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/../../frontend/src/$1'
  },
  setupFilesAfterEnv: ['<rootDir>/setupTests.ts'],
  extensionsToTreatAsEsm: ['.ts', '.tsx'],
  globals: { 'ts-jest': { tsconfig: '<rootDir>/tsconfig.json', useESM: true } }
};
