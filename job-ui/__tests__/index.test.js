import { render, screen, waitFor } from '@testing-library/react';
import Languages from '../src/app/components/Languages';
import Result from '../src/app/components/Result'

jest.mock('localhost:8000/api', () => ({
    fetchData: jest.fn(() => Promise.resolve( [{all_languages: ['Python']}, [{ title: '1', url: '2', programming_langauges: ['Python']}]] )),
}));

test('renders data from backend', async () => {
  render(<Languages />);

  // Wait for the asynchronous data fetching to complete
  await waitFor(() => expect(fetchData).toHaveBeenCalled());

  // Ensure that the component renders the data
  expect(screen.getByText('Python')).toBeInTheDocument();
});

test('renders job listings', async () => {
    render(<Result />);
  
    // Wait for the asynchronous data fetching to complete
    await waitFor(() => expect(fetchData).toHaveBeenCalled());
  
    // Ensure that the component renders the data
    expect(screen.getByText('Python')).toBeInTheDocument();

    expect(screen.getByText('1')).toBeInTheDocument();

    expect(screen.getByText('2')).toBeInTheDocument();
});