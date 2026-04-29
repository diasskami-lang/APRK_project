const { Pool } = require('pg');

const pool = new Pool({
  host: 'localhost',
  database: 'test_gov_1',
  user: 'postgres',
  password: '1234',
  port: 5433,
});

pool.on('error', (error) => {
  console.error('Unexpected PostgreSQL error:', error.message);
});

module.exports = pool;

