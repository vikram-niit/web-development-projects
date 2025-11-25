import React from 'react';
import { deleteTask } from '../services/api';

export default function TaskList({ tasks, refreshTasks }) {
    const handleDelete = async (id) => {
        await deleteTask(id);
        refreshTasks();
    };

    return (
        <ul>
            {tasks.map(task => (
                <li key={task._id}>
                    {task.title}
                    <button onClick={() => handleDelete(task._id)}>Delete</button>
                </li>
            ))}
        </ul>
    );
}
