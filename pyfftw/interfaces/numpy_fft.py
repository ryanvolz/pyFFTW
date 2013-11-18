#!/usr/bin/env python
#
# Copyright 2013 Knowledge Economy Developments Ltd
# 
# Henry Gomersall
# heng@kedevelopments.co.uk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
This module implements those functions that replace aspects of the
:mod:`numpy.fft` module. This module *provides* the entire documented namespace 
of :mod:`numpy.fft`, but those functions that are not included here are imported
directly from :mod:`numpy.fft`.


It is notable that unlike :mod:`numpy.fftpack`, these functions will 
generally return an output array with the same precision as the input
array, and the transform that is chosen is chosen based on the precision
of the input array. That is, if the input array is 32-bit floating point,
then the transform will be 32-bit floating point and so will the returned
array. If any type conversion is required, the default will be double
precision.

One known caveat is that repeated axes are handled differently to
:mod:`numpy.fft`; axes that are repeated in the axes argument are considered
only once, as compared to :mod:`numpy.fft` in which repeated axes results in
the DFT being taken along that axes as many times as the axis occurs.

The exceptions raised by each of these functions are mostly as per their
equivalents in :mod:`numpy.fft`, though there are some corner cases in
which this may not be true.
'''

from ._utils import _Xfftn

# Complete the namespace (these are not actually used in this module)
from numpy.fft import fftfreq, fftshift, ifftshift
import numpy

__all__ = ['fft','ifft', 'fft2', 'ifft2', 'fftn', 'ifftn', 
           'rfft', 'irfft', 'rfft2', 'irfft2', 'rfftn', 'irfftn',
           'hfft', 'ihfft', 'fftfreq', 'fftshift', 'ifftshift']

def fft(a, n=None, axis=-1, overwrite_input=False, 
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 1D FFT.
    
    The first three arguments are as per :func:`numpy.fft.fft`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''

    calling_func = 'fft'

    return _Xfftn(a, n, axis, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def ifft(a, n=None, axis=-1, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 1D inverse FFT.
    
    The first three arguments are as per :func:`numpy.fft.ifft`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'ifft'

    return _Xfftn(a, n, axis, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)


def fft2(a, s=None, axes=(-2,-1), overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 2D FFT.
    
    The first three arguments are as per :func:`numpy.fft.fft2`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'fft2'

    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def ifft2(a, s=None, axes=(-2,-1), overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 2D inverse FFT.
    
    The first three arguments are as per :func:`numpy.fft.ifft2`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'ifft2'

    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)


def fftn(a, s=None, axes=None, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform an n-D FFT.
    
    The first three arguments are as per :func:`numpy.fft.fftn`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'fftn'

    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def ifftn(a, s=None, axes=None, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform an n-D inverse FFT.
    
    The first three arguments are as per :func:`numpy.fft.ifftn`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'ifftn'

    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def rfft(a, n=None, axis=-1, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 1D real FFT.
    
    The first three arguments are as per :func:`numpy.fft.rfft`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'rfft'

    return _Xfftn(a, n, axis, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def irfft(a, n=None, axis=-1, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 1D real inverse FFT.
    
    The first three arguments are as per :func:`numpy.fft.irfft`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'irfft'

    return _Xfftn(a, n, axis, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def rfft2(a, s=None, axes=(-2,-1), overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 2D real FFT.
    
    The first three arguments are as per :func:`numpy.fft.rfft2`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'rfft2'

    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def irfft2(a, s=None, axes=(-2,-1), overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 2D real inverse FFT.
    
    The first three arguments are as per :func:`numpy.fft.irfft2`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'irfft2'
    
    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)


def rfftn(a, s=None, axes=None, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform an n-D real FFT.
    
    The first three arguments are as per :func:`numpy.fft.rfftn`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'rfftn'

    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)


def irfftn(a, s=None, axes=None, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform an n-D real inverse FFT.
    
    The first three arguments are as per :func:`numpy.fft.rfftn`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''
    calling_func = 'irfftn'
    
    return _Xfftn(a, s, axes, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func)

def hfft(a, n=None, axis=-1, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 1D FFT of a signal with hermitian symmetry.
    This yields a real output spectrum. See :func:`numpy.fft.hfft`
    for more information.

    The first three arguments are as per :func:`numpy.fft.hfft`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''

    # The hermitian symmetric transform is equivalent to the 
    # irfft of the conjugate of the input (do the maths!) without
    # any normalisation of the result (so normalise_idft is set to 
    # False).
    a = numpy.conjugate(a)

    calling_func = 'irfft'

    return _Xfftn(a, n, axis, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous, 
            calling_func, normalise_idft=False)

def ihfft(a, n=None, axis=-1, overwrite_input=False,
        planner_effort='FFTW_MEASURE', threads=1,
        auto_align_input=True, auto_contiguous=True):
    '''Perform a 1D inverse FFT of a real-spectrum, yielding
    a signal with hermitian symmetry. See :func:`numpy.fft.ihfft`
    for more information.
    
    The first three arguments are as per :func:`numpy.fft.ihfft`; 
    the rest of the arguments are documented 
    in the :ref:`additional arguments docs<interfaces_additional_args>`.
    '''

    # Result is equivalent to the conjugate of the output of
    # the rfft of a.
    # It is necessary to perform the inverse scaling, as this
    # is not done by rfft.
    if n is None:
        if not isinstance(a, numpy.ndarray):
            a = numpy.asarray(a)

        n = a.shape[axis]

    scaling = 1.0/n

    return scaling * rfft(a, n, axis, overwrite_input, planner_effort,
            threads, auto_align_input, auto_contiguous).conj()
