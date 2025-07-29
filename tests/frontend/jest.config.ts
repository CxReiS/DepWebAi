import path from 'path';

const config = {
  rootDir: path.resolve(__dirname, '../../frontend'),
  preset: path.resolve(__dirname, '../../frontend/node_modules/ts-jest/presets/default-esm'),
  testEnvironment: 'jsdom',
  extensionsToTreatAsEsm: ['.ts', '.tsx'],
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '^react-router-dom$': '<rootDir>/tests/frontend/__mocks__/react-router-dom.tsx'
  },
  moduleDirectories: ['node_modules', path.resolve(__dirname, '../../frontend/node_modules')],
  setupFilesAfterEnv: ['<rootDir>/../tests/frontend/setupTests.ts'],
  roots: ['<rootDir>', '<rootDir>/../tests/frontend'],
  testMatch: [
    '<rootDir>/src/**/?(*.)+(spec|test).[tj]s?(x)',
    '<rootDir>/../tests/frontend/react-testing-library/**/?(*.)+(spec|test).[tj]s?(x)'
  ],
  collectCoverageFrom: ['<rootDir>/src/**/*.{ts,tsx}'],
  coverageDirectory: '<rootDir>/../tests/frontend/coverage',
  globals: {
    'ts-jest': {
      tsconfig: path.resolve(__dirname, 'tsconfig.json'),
      diagnostics: false
    }
  }
};

export default config;
