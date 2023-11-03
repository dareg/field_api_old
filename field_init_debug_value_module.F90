! (C) Copyright 2022- ECMWF.
! (C) Copyright 2022- Meteo-France.
!
! This software is licensed under the terms of the Apache Licence Version 2.0
! which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
! In applying this licence, ECMWF does not waive the privileges and immunities
! granted to it by virtue of its status as an intergovernmental organisation
! nor does it submit to any jurisdiction.

MODULE FIELD_INIT_DEBUG_VALUE_MODULE
  USE PARKIND1
  LOGICAL :: USE_INIT_DEBUG_VALUE = .FALSE.
  REAL(KIND=JPRM) :: INIT_DEBUG_VALUE_JPRM = 0.0_JPRM
  REAL(KIND=JPRB) :: INIT_DEBUG_VALUE_JPRB = 0.0_JPRB
  REAL(KIND=JPRD) :: INIT_DEBUG_VALUE_JPRD = 0.0_JPRD
  INTEGER(KIND=JPIM) :: INIT_DEBUG_VALUE_JPIM = 0_JPIM
  LOGICAL(KIND=JPLM) :: INIT_DEBUG_VALUE_JPLM = .FALSE.
END MODULE FIELD_INIT_DEBUG_VALUE_MODULE
