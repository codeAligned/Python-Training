from nose.tools import *
from ex48.parser import *

def test_peek():
    assert_equal(peek([('noun','bear'),('verb','run')]), 'noun')
    assert_equal(peek([]), None)

def test_match():
    assert_equal(match([('verb','run'),('noun','bear')], 'verb'), ('verb','run'))
    assert_equal(match([],'noun'), None)
    assert_equal(match([('noun', 'bear')], 'verb'), None)

def test_parse_verb():
    assert_equal(
        parse_verb([
            ('stop', 'the'),
            ('stop', 'the'),
            ('stop', 'of'),
            ('verb', 'run')
        ]),('verb', 'run')
    )
    assert_raises(ParserError, parse_verb, [('noun', 'bear')])

def test_parse_object():
    assert_equal(
        parse_object([
            ('stop', 'the'),
            ('noun', 'bear'),
            ('stop', 'of'),
            ('verb', 'run')
        ]),('noun', 'bear')
    )
    assert_raises(ParserError, parse_object, [('verb', 'run')])

def test_parse_subject():
    assert_equal(
        parse_subject([
            ('stop', 'the'),
            ('noun', 'bear'),
            ('stop', 'of'),
            ('verb', 'run')
        ]),('noun', 'bear')
    )
    assert_raises(ParserError, parse_subject, [('stop', 'the')])

def test_parse_sentence():
    testSentence = parse_sentence([
        ('verb', 'run'),
        ('direction', 'north')])
    assert_equal((testSentence.subject ,testSentence.verb, testSentence.object)
    ,('player','run','north'))
