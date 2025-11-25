import React, { useState, useEffect } from 'react';
import { getTasks } from '../services/api';
import TaskForm from '../components/TaskForm';
import TaskList from '../components/TaskList';

export default function Home() {
    const [tasks, setTasks] = useState([]);

    const fetchTasks = async () => {
        const res = await getTasks();
        setTasks(res.data);
    };

    useEffect(() => {
        fetchTasks();
    }, []);

    return (
        <div>
            <h1>Task Manager</h1>
            <TaskForm onTaskAdded={fetchTasks} />
            <TaskList tasks={tasks} refreshTasks={fetchTasks} />
        </div>
    );
}
