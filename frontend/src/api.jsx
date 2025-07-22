import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const uploadDocument = (file) => {
  const formData = new FormData();
  formData.append('file', file);
  return axios.post(`${BASE_URL}/upload/`, formData);
};

export const queryAnswer = (question) => {
  const formData = new FormData();
  formData.append('question', question);
  return axios.post(`${BASE_URL}/query/`, formData);
};
