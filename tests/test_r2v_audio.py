from pathlib import Path
import importlib.util
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/creative-ad-director/scripts/validate_r2v_audio.py'
spec = importlib.util.spec_from_file_location('r2v_guard', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def payload(*durations):
    return {'model': 'dreamina-seedance-2-5', 'mode': 'r2v',
            'required_roles': [f'CH{i}' for i in range(len(durations))],
            'audio': [{'role_id': f'CH{i}', 'asset_id': f'actual-{i}',
                       'duration_seconds': d, 'duration_verified': True,
                       'source_approved': True, 'purpose': 'voice_reference'}
                      for i, d in enumerate(durations)]}


class AudioGuardTests(unittest.TestCase):
    def test_rejects_reported_short_audio(self):
        self.assertFalse(module.validate_manifest(payload(1.79))['ready_to_submit'])

    def test_accepts_inclusive_minimum_with_margin_warning(self):
        result = module.validate_manifest(payload('1.8'))
        self.assertTrue(result['ready_to_submit'])
        self.assertTrue(result['warnings'])

    def test_rejects_two_full_twenty_second_auditions(self):
        result = module.validate_manifest(payload(20, 20))
        self.assertFalse(result['ready_to_submit'])
        self.assertEqual(result['total_audio_seconds'], 40)

    def test_accepts_inclusive_total_using_decimal_arithmetic(self):
        self.assertTrue(module.validate_manifest(payload('15.1', '15.1'))['ready_to_submit'])
        self.assertFalse(module.validate_manifest(payload('15.1', '15.1001'))['ready_to_submit'])

    def test_accepts_short_role_specific_references(self):
        result = module.validate_manifest(payload(6, 6, 6))
        self.assertTrue(result['ready_to_submit'])
        self.assertFalse(result['warnings'])

    def test_does_not_deduplicate_away_outgoing_audio_duration(self):
        data = payload(20, 20)
        data['audio'][1]['asset_id'] = data['audio'][0]['asset_id']
        result = module.validate_manifest(data)
        self.assertFalse(result['ready_to_submit'])
        self.assertEqual(result['total_audio_seconds'], 40)

    def test_missing_or_wrong_speaker_is_not_ready(self):
        data = payload(6)
        data['required_roles'].append('narrator')
        self.assertFalse(module.validate_manifest(data)['ready_to_submit'])
        data = payload(6)
        data['audio'][0]['role_id'] = 'someone-else'
        self.assertFalse(module.validate_manifest(data)['ready_to_submit'])

    def test_unmeasured_or_unapproved_asset_is_not_ready(self):
        for field in ['duration_verified', 'source_approved']:
            data = payload(6)
            data['audio'][0][field] = False
            self.assertFalse(module.validate_manifest(data)['ready_to_submit'])

    def test_invalid_durations_fail_closed(self):
        for value in [None, True, 'NaN', 'Infinity', -1, 0, 'not measured']:
            with self.subTest(value=value):
                self.assertFalse(module.validate_manifest(payload(value))['ready_to_submit'])

    def test_silent_request_and_wrong_mode(self):
        self.assertTrue(module.validate_manifest(payload())['ready_to_submit'])
        data = payload(6)
        data['mode'] = 'unknown'
        self.assertFalse(module.validate_manifest(data)['ready_to_submit'])

    def test_counts_voice_reference_and_dialogue_together(self):
        data = payload(6)
        data['audio'].append({**data['audio'][0], 'asset_id': 'final-line',
                              'purpose': 'dialogue', 'duration_seconds': 25})
        self.assertFalse(module.validate_manifest(data)['ready_to_submit'])

    def test_malformed_structure_has_a_result_not_a_crash(self):
        for data in [None, [], {}, {'required_roles': [None], 'audio': [None]}]:
            self.assertFalse(module.validate_manifest(data)['ready_to_submit'])


if __name__ == '__main__':
    unittest.main()
