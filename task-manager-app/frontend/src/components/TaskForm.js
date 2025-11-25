import React, { useState } from 'react';
import { createTask } from '../services/api';

export default function TaskForm({ onTaskAdded }) {
    const [title, setTitle] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!title) return;
        await createTask({ title });
        setTitle('');
        onTaskAdded();
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Add a task"
            />
            <button type="submit">Add</button>
        </form>
    );
}
