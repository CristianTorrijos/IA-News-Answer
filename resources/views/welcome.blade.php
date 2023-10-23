<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Search</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>

<body class="bg-gray-200 h-screen flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-xl w-96">
        <form method="post" action="/api/search" class="flex flex-col">
            <span class="text-lg font-semibold text-gray-700">You can try our API here</span>
            <input type="text" name="query" placeholder="Enter your search query..."
                   class="p-3 rounded-md border border-gray-300 mb-4 focus:outline-none focus:border-indigo-500">
            <button type="submit"
                    class="bg-indigo-600 text-white p-3 rounded-md hover:shadow-lg transition-shadow duration-300 ease-in-out">
                Search
            </button>
        </form>
    </div>
</body>
</html>
