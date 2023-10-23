<?php

namespace App\Http\Controllers;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

use Illuminate\Http\Request;

class ApiSearchController extends Controller
{
    public function index(Request $request) {
        $bp = base_path();
        $process = new Process([$bp . '/python/pruebaCristianTorrijosIA/bin/python3', $bp . '/python/search.py', $request->input('query')]);

        try {
            $process->mustRun();
            $output = json_decode($process->getOutput());
            return response()->json($output);

        } catch (ProcessFailedException $exception) {
            return response()->json(['error' => $exception->getMessage()]);
        }
    }
}
