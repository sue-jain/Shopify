
const express = require('express');
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// In-memory "database"
let todos = [
    { id: 1, task: 'Initial to-do' }
];

// GET /todos - Retrieve all to-do items
app.get('/todos', (req, res) => {
    res.status(200).json(todos);
});

// POST /todos - Create a new to-do item
app.post('/todos', (req, res) => {
    const { task } = req.body;

    // Error path: No task provided
    if (!task) {
        return res.status(400).json({ error: 'Task is required' });
    }

    // Happy path: Create new to-do
    const newTodo = {
        id: todos.length + 1,
        task
    };
    todos.push(newTodo);
    res.status(201).json(newTodo);
});

module.exports = app; // Export for testing
