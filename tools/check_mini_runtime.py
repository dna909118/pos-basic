#!/usr/bin/env python3
"""Exercise the pinned mini-SWE/LiteLLM tool-call path without API access."""
import json
import os
import tempfile
from importlib.metadata import version
from unittest.mock import patch


def check_runtime():
    command = 'printf offline-runtime-check'
    tool_call = {
        'id': 'offline_tool_call',
        'type': 'function',
        'function': {'name': 'bash', 'arguments': json.dumps({'command': command})},
    }
    with tempfile.TemporaryDirectory(prefix='byar-mini-check-') as config_dir:
        with patch.dict(os.environ, {
            'MSWEA_GLOBAL_CONFIG_DIR': config_dir,
            'MSWEA_SILENT_STARTUP': '1',
            'LITELLM_LOCAL_MODEL_COST_MAP': 'True',
        }), patch('socket.socket.connect', side_effect=AssertionError('Offline check forbids network access')):
            from minisweagent.models import get_model

            model = get_model('deepseek/deepseek-chat', {
                'model_kwargs': {
                    'mock_response': 'Offline runtime check',
                    'mock_tool_calls': [tool_call],
                },
            })
            # Use the real provider setup/import path; only its response is mocked.
            # Bypass retry handling so missing dependencies fail immediately.
            response = model._query([{'role': 'user', 'content': 'Offline tool-call check'}])
            actions = model._parse_actions(response)
            if len(actions) != 1 or actions[0]['command'] != command:
                raise AssertionError('Mock tool call was not parsed into the expected action')
            # Parsing an action does not execute it or run a coding agent.
    return {
        'status': 'PASS',
        'mini_swe_agent': version('mini-swe-agent'),
        'litellm': version('litellm'),
        'mcp': version('mcp'),
        'tool_call_parsed': True,
        'response': 'mocked',
        'commands_executed': 0,
    }


if __name__ == '__main__':
    print(json.dumps(check_runtime(), indent=2))
