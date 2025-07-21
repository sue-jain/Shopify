
const request = require('supertest');
const app = require('./app');

describe('To-Do API', () => {

    // Test suite for GET /todos
    describe('GET /todos', () => {
        it('should return a list of to-do items', async () => {
            const response = await request(app).get('/todos');
            expect(response.statusCode).toBe(200);
            expect(response.body).toBeInstanceOf(Array);
            expect(response.body.length).toBeGreaterThan(0);
        });
    });

    // Test suite for POST /todos
    describe('POST /todos', () => {
        // Happy path test
        it('should create a new to-do item when a task is provided', async () => {
            const newTodo = { task: 'Test a POST request' };
            const response = await request(app)
                .post('/todos')
                .send(newTodo);
            
            expect(response.statusCode).toBe(201);
            expect(response.body.task).toBe(newTodo.task);
            expect(response.body).toHaveProperty('id');
        });

        // Error path test
        it('should return a 400 error if the task is missing', async () => {
            const response = await request(app)
                .post('/todos')
                .send({}); // Sending an empty body
            
            expect(response.statusCode).toBe(400);
            expect(response.body).toHaveProperty('error');
        });
    });

});
